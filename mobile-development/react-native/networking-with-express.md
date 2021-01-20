# Networking with Express

Server:

```typescript
import express from 'express';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors());

app.get('/', (req, res) => {
  res.send({'text': 'Hello World!'})
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});
```

App:

```typescript
import React, { useState } from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';

export default function App() {
  const [text, setText] = useState('')

  return (
    <View style={styles.container}>
      <Button
        title={'Press'}
        onPress={async () => {
          var body = await http('http://localhost:3000/');
          var text: string = body.text;
          setText(text);
        }}
      />
      <Text>{text}</Text>
    </View>
  );
}

async function http(url: string): Promise<any> {
  const response = await fetch(url);
  const body = await response.json();
  return body;
}
```
