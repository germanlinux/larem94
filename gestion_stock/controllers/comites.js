// controleur comites
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db');

// SEPARATEUR
exports.dotation= function(req, res){

  var madate = new Date();
  var jour=madate.getDate();
  var mois=madate.getMonth()+1;
  var an=madate.getFullYear();
  strdate =an+ '-' + mois + '-' + jour
  db.connect(function(){console.log('connection base depuis:',scriptName)
    });
  console.log('body',req.body);
  // recup des parametes
  // niveau dotation
  //
  let depot = req.body._depot;
  let produit = Number(req.body._id_produit);
  let dotation = Number(req.body._dotation);
  let total  = Number(req.body._total);
  console.log(depot, produit, dotation, total,strdate );
  // creation dotation
  db.get().one("INSERT INTO dotations (depot, produit, datedotation, quantite_initiale, quantite_reservee) VALUES ($1, $2, $3, $4, $5) RETURNING id_dotation",[depot, produit,strdate, dotation, total] )
    .then((data)=> {
      console.log('id', data.id_dotation);
      // insert pour chacun des comites
       let tabcomite =[];
       let tabkeys = Object.keys(req.body);
       console.log('er',tabkeys);
       db.get().task(t => {
         for(i=0; i < tabkeys.length;i++){
           if(tabkeys[i][0] != '_') {
             let comite = tabkeys[i];
             let quantite = Number(req.body[tabkeys[i]]);
             tabcomite.push(db.get().none("INSERT INTO repartitions (dotation, depot, produit, datedotation, quantite_initiale, comite)  \
             Values ($1,$2,$3, $4, $5, $6)",[data.id_dotation, depot, produit, strdate, quantite, comite]  ));
           }
          }
        return t.batch(tabcomite)
       .then(() => {
          console.log('OK');
          res.send("e---------------g");
       })
       })
     })

}
exports.update = function(req, res){
    db.connect(function(){console.log('connection base depuis:',scriptName)
    });
    let myid = req.params.id;
    let mylibelle = req.body.libelle;
    let mydepot =  req.body.depot;
    db.get().none("update comites set libelle=$1 , id_depot = $2 where id_comite=$3",[mylibelle, mydepot, myid] )
    .then(()=> {
    res.redirect('/comite_liste');
     })
    .catch(error => {
        console.log(error);
    })
    };



// SEPARATEUR
exports.edit = function(req, res){
    db.connect(function(){console.log('connection base depuis:',scriptName)
    });
    myid = req.params.id;
    console.log(myid)    ;
    db.get().task(t => {
      const q1 = db.get().one('select * from comites where id_comite= $1',myid);
      const q2 = db.get().any('select * from depots order by nom');
      return t.batch([q2,q1])
    .then(data => {
      data[1]['title']= 'Stock laREM94';
      data[1]['depots'] = data[0];
      console.log('eric',data[1]);
      res.render('comite',data[1]);
    })
    .catch(error => {
        console.log(error);
    })
    });
};
// SEPARATEUR

exports.liste= function(req, res, next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });

  var hub;
  db.get().task(t => {
    const q1 =   t.any('select id_comite,libelle,id_depot from comites  order by code_interne,id_depot;');
    return t.batch([q1])
  .then(data => {
     console.log('eg', data);

     let eg = data.shift();
     console.log(typeof(eg))
     let dt1 =[];
     let dt2 =[];
     let dt3 =[];
     let dt4 =[];
     let dt5 =[];

    /* let dt5 =[];*/
     console.log('er',eg[0].id_depot);
     for (i=0; i<eg.length;i++){
      item = eg[i];
      console.log('ee',item)
      switch(item.id_depot) {

        case 'T10':
          dt1.push(item);
          break;
        case 'T10.1':
          dt2.push(item);
          break;
        case 'T11':
          dt3.push(item);
          break;
        case 'T12':
          dt4.push(item);
          break;
       case 'A suivre':
          dt5.push(item);
          break;


       }
     };
  console.log('eric',dt1);
  res.render('comitelist', { title: 'Stock laREM94'  ,t1: dt1,t2: dt2,t3: dt3, t4: dt4, t5: dt5  });
    })
    })
  .catch(error => {
        console.log(error);
    });

};
