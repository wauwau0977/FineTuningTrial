For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java' with name 'MavenWrapperDownloader.java' where below a part of it is displayed...
```java
private static final String PROPERTY_NAME_WRAPPER_URL = "wrapperUrl";
public static void main(String args[]) {
    System.out.println("- Downloader started");
    File baseDirectory = new File(args[0]);
    System.out.println("- Using base directory: " + baseDirectory.getAbsolutePath());
    // If the maven-wrapper.properties exists, read it and check if it contains a custom
    // wrapperUrl parameter.
    File mavenWrapperPropertyFile = new File(baseDirectory, MAVEN_WRAPPER_PROPERTIES_PATH);
    String url = DEFAULT_DOWNLOAD_URL;
    if (mavenWrapperPropertyFile.exists()) {
        FileInputStream mavenWrapperPropertyFileInputStream = null;
        try {
            mavenWrapperPropertyFileInputStream = new FileInputStream(mavenWrapperPropertyFile);
            Properties mavenWrapperProperties = new Properties();
            mavenWrapperProperties.load(mavenWrapperPropertyFileInputStream);
            url = mavenWrapperProperties.getProperty(PROPERTY_NAME_WRAPPER_URL, url);
        } catch (IOException e) {
            System.out.println("- ERROR loading '" + MAVEN_WRAPPER_PROPERTIES_PATH + "'");
        } finally {
            try {
                if (mavenWrapperPropertyFileInputStream != null) {
                    mavenWrapperPropertyFileInputStream.close();
                }
            } catch (IOException e) {
                // Ignore ...
            }
        }
    }
    System.out.println("- Downloading from: : " + url);
```
What is the purpose of the `getProperty(PROPERTY_NAME_WRAPPER_URL, url)` method call within the `if (mavenWrapperPropertyFile.exists())` block, and what are its arguments? Explain what happens if the property `wrapperUrl` is found, and what happens if it's not found in the `maven-wrapper.properties` file.