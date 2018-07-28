var express = require('express');
var router = express.Router();
var db  =require('../db');
/* GET home page. */
router.get('/', function(req, res, next) {
 db.connect(function(){console.log('connection base depuis maj');
  });
  db.get().any("select id_evenement,to_char(dateevenement,'DD/MM/YYYY') as  dateevenement, a.libelle, b.url from evenements as A  join comites_06_2018 as B on A.id_comite = B.id_comite where A.type is Null order by dateevenement; " )
  .then((data)=> {
         console.log(data);
         res.render('partial_hdp', { title: 'Express', eves : data });
   })
  .catch(error => {
           console.log(error);
         })
})
router.post('/maj', function(req, res, next) {
  for (let item  in req.body ) {
    valeur =  req.body[item];
    id = item
  }
  db.connect(function(){console.log('connection base depuis maj');
  });
  db.get().none("update  evenements set type = $1 where  id_evenement = $2;",[valeur, id])
  .then(()=> {
    res.redirect('/');
   })
  .catch(error => {
           console.log(error);
         })


})
module.exports = router;
/*
<form v-on:change="formOnChange">
    <select>
        <!--  code --->
    </select>
</form>
*/
