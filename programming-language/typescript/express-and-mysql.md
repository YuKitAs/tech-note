# Express and MySQL

Install `mysql` and `@types/mysql` and import:

```typescript
import mysql from 'mysql';
```

Set up connection:

```typescript
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'test',
  password: 'test',
  database: 'test'
});

connection.connect();
```

Read and write queries (assuming table `users` has an auto-incremented integer `id` and a `username`):

```typescript
async function saveUser(username: string): Promise<number> {
  const id: number = await new Promise((resolve, reject) => {
    connection.query('INSERT INTO users SET username=?', username, (err, res, fields) => {
      if (err) { reject(err); return; }
      resolve(res.insertId);
    });
  });
  return id;
}

async function getUsername(id: number): Promise<string> {
  const username: string = await new Promise((resolve, reject) => {
    connection.query('SELECT username FROM users WHERE id=?', id, (err, res, fields) => {
      if (err) { reject(err); return; }
      resolve(res[0].username);
    });
  });
  return username;
}
```
