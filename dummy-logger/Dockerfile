FROM alpine

ENV LOGFILE="/log"

# Install GNU version of tail
RUN ["apk", "add", "-U", "coreutils"]

# `-F` here follows the filename and not the file descriptor, and also adds a retry in case the file doesn't exist yet.
CMD ["sh", "-c", "tail -F $LOGFILE"]
