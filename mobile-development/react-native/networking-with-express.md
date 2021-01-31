# Networking with Express

## JSON Response

Server:

```typescript
import express from 'express';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors());

app.get('/', (req, res) => {
  res.send({'text': 'Hello World!'});
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

App:

```typescript
import React, { useState } from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';

export default function App() {
  const [text, setText] = useState('');

  return (
    <View style={styles.container}>
      <Button
        title={'Press'}
        onPress={async () => {
          const response = await fetch('http://localhost:3000/');
          const body = await response.json();
          var text: string = body.text;
          setText(text);
        }}
      />
      <Text>{text}</Text>
    </View>
  );
}
```

## Blob Response

Server:

```typescript
app.get('/', (req, res) => {
  res.sendFile('/path/to/file');
});
```

App:

```typescript
import React, { useState } from 'react';
import { Button, Image, StyleSheet, View } from 'react-native';

export default function App() {
  const [file, setFile] = useState('');

  return (
    <View style={styles.container}>
      <Button
        title={'Press'}
        onPress={async () => {
          const response = await fetch('http://localhost:3000/');
          const body = await response.blob();
          setFile(URL.createObjectURL(body));
        }}
      />
    </View>
  );
}
```
