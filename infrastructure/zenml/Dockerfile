FROM zenmldocker/zenml:0.81.0-py3.12

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the cert.pem file into the image
COPY "certs/AXA-Enterprise-Root-CA.pem" "/usr/local/share/ca-certificates/AXA-Enterprise-Root-CA.crt"
RUN update-ca-certificates
