import fs from 'fs'

// const data = fs.readFileSync('/example.txt', 'utf8');

fs.readFile('js_fs/example.txt',(err, data) => {
  if (err) throw err;
  console.log(data);
});

// print(data)


type='module'