FROM eclipse-temurin:17.0.6_10-jdk-jammy

# Set WORKDIR
WORKDIR /opt/helloworld

# EXPOSE the server port
EXPOSE 8080/tcp

# COPY needed files and directories to WORKDIR
COPY src ./src
COPY gradle ./gradle
COPY gradlew settings.gradle build.gradle ./

# Build the application
RUN ./gradlew clean build 

# Set ENTRYPOINT for the container
ENTRYPOINT ["java", "-jar", "/opt/helloworld/build/libs/helloworld.jar"]
