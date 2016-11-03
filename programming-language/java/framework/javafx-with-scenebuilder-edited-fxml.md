# JavaFX with SceneBuilder edited FXML

  1. Load FXML file
  
  Create a `Main` class which extends `javax.application.Application`.
  
  Add the following code into the `start(Stage primaryStage)` method to load the FXML file and make it as root in a stage's scene.
  
  ```java
  Parent root = FXMLLoader.load(Main.class.getResource("example.fxml"));
  Scene scene = new Scene(root, 300, 275);
  primaryStage.setTitle("Hello World!");
  primaryStage.setScene(scene);
  primaryStage.show();
  ```
  
  2. Controller for FXML
  
  Create a `Controller` class which implements the `Initializable` interface.
  
  Define a `fx:id` to an object, either in SceneBuilder or in the FXML file. Here we "add `fx:id="myButton"` to a button for example.
  
  Then, add `fx:controller="Controller"` to the root object in the `example.fxml` and declare `@FXML private Button myButton` in the `Controller` class, so that the value of `myButton` will be injected by `FXMLLoader`.
  
  Initialize the logic in the `initialize` method, for example the action handler with `myButton`. All `@FXML` variables will be injected.

&nbsp;

Find more tutorials for JavaFX [here](http://docs.oracle.com/javase/8/javafx/get-started-tutorial/get_start_apps.htm#BACECIIB).
