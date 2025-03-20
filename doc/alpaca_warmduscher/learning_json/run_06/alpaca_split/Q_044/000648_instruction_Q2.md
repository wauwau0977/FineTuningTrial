For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java' with name 'MavenWrapperDownloader.java'... 
Consider the `downloadFileFromURL` method:

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

What potential exceptions could occur within this method and how could they be handled more gracefully?