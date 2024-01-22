const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

app.use(cors());
app.use(bodyParser.json());

const db = mysql.createConnection({
  host: 'localhost',
  user: 'BobcatClawsDev',
  password: 'CS#4398DB',
  database: 'BobcatClawsDB'
});

app.get('/api/table', (req, res) => {
  db.query('SELECT * FROM Product', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});
