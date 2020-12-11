const express = require("express")
const compression = require("compression")
const bodyParser = require("body-parser")
const _where = require("lodash.where")
const sql = require('mssql');
const app = express()
app.use(bodyParser.json())
app.use(compression())
const server = app.listen(3000, a=> {
    console.log('listening at http://localhost:3000')
})

const { Pool } = require('pg')
const pool = new Pool({
  user: 'bootcamp',
  host: '206.189.80.195',
  database: 'bootcamp',
  password: 'Bootcamp*123',
  port: 5432,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
})

app.use('/', express.static('./public'));
//untuk handle input dari client
// app.use(express.json)
app.use(express.urlencoded())

app.get('/',function(req,res){
    res.send('hello dunia')
})

app.get('/json',function(req,res){
    var data = [{"Nama":"Alfi"}]
    res.send(data)
})

app.get('/api/jawaban/3', function(req,res){
    pool.connect((err, client, done) => {
        if (err) throw err
        client.query(`select "Region", count("Country") as "TotalCountry" 
                        from 
                        (select "Region" , "Country" from bootcamp_test_alfi group by "Region","Country") 
                        as tb2
                        group by "Region"`
                        , (err, result) => {
          done()
          if (err) {
            console.log(err.stack)
          } else {
            res.send(result['rows'])
            console.log(result)
          }
        })
      })
})

app.get('/api/jawaban/4', function(req,res){
    pool.connect((err, client, done) => {
        if (err) throw err
        client.query(`select "Country" , "Year" , max("AvgTemperature"), min("AvgTemperature") 
        from bootcamp_test_alfi 
        where ("Country" = 'Canada' or "Country" = 'Malaysia' or "Country"='Turkey') and "Year" = 2018 group by "Country", "Year" `
                        , (err, result) => {
          done()
          if (err) {
            console.log(err.stack)
          } else {
            res.send(result['rows'])
            console.log(result)
          }
        })
      })
})

app.get('/api/jawaban/5', function(req,res){
    pool.connect((err, client, done) => {
        if (err) throw err
        client.query(`select "Region" ,"Country" , "AvgTemperature" 
        from (
            select "Region", "Country", "AvgTemperature", "Day", "Month" , "Year" , Rank()
                over (partition by "Region" order by "AvgTemperature" desc) as rn 
                from bootcamp_test_alfi where "Day" = 1 and "Month" = 10 and "Year" = 2012
        ) as t2 where rn <=5 `
                        , (err, result) => {
          done()
          if (err) {
            console.log(err.stack)
          } else {
            res.send(result['rows'])
            console.log(result)
          }
        })
      })
})