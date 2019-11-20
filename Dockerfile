ARG PARENT_IMAGE
ARG USE_GPU
FROM $PARENT_IMAGE

RUN apt-get -y update \
    && apt-get -y install \
    curl \
    cmake \
    default-jre \
    git \
    jq \
    python-dev \
    python-pip \
    python3-dev \
    libfontconfig1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libopenmpi-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV CODE_DIR /root/code
ENV VENV /root/venv

COPY ./setup.py /root/code/setup.py
RUN \
    mkdir -p ${CODE_DIR}/stable_baselines && \
    pip install virtualenv && \
    virtualenv $VENV --python=python3 && \
    . $VENV/bin/activate && \
    cd $CODE_DIR && \
    pip install --upgrade pip && \
    if [[ $USE_GPU == "True" ]]; then \
        TENSORFLOW_PACKAGE="tensorflow-gpu==1.8.0"; \
    else \
        TENSORFLOW_PACKAGE="tensorflow==1.8.0"; \
    fi; \
    pip install ${TENSORFLOW_PACKAGE} && \
    pip install -e .[mpi,tests] && \
    pip install codacy-coverage && \
    rm -rf $HOME/.cache/pip

ENV PATH=$VENV/bin:$PATH

# Codacy code coverage report: used for partial code coverage reporting
RUN cd $CODE_DIR && \
    curl -Ls -o codacy-coverage-reporter.jar "$(curl -Ls https://api.github.com/repos/codacy/codacy-coverage-reporter/releases/latest | jq -r '.assets | map({name, browser_download_url} | select(.name | (contains("codacy-coverage-reporter") and endswith("assembly.jar")))) | .[0].browser_download_url')"

CMD /bin/bash
