For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java' with name 'MavenWrapperDownloader.java'... 
The main method starts with:

```java
System.out.println("- Downloader started");
File baseDirectory = new File(args[0]);
System.out.println("- Using base directory: " + baseDirectory.getAbsoleutePath());
```

What is the purpose of `args[0]` and what potential issues could arise if the `args` array is empty or contains invalid data? How could this be handled more robustly?