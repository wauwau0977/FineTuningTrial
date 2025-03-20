For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java' with name 'MavenWrapperDownloader.java' where below a part of it is displayed...
```java
private static void downloadFileFromURL(String urlString, File destination) throws Exception {
    URL website = new URL(urlString);
    ReadableByteChannel rbc;
    rbc = Channels.newChannel(website.openStream());
    FileOutputStream fos = new FileOutputStream(destination);
    fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
    fos.close();
    rbc.close();
}
```
Explain the purpose of the `downloadFileFromURL` method, detailing how it downloads a file from a given URL to a specified destination file, and what the roles of `ReadableByteChannel` and `FileOutputStream` are in this process. What is the potential risk of not properly closing the channels and streams?