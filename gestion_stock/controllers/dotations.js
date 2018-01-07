// controleur dotations
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db');

// SEPARATEUR

//get rservation
exports.a_retirer = function(req, res){
 let dotation = req.params.id;
// console.log('eg',dotation);
 console.log('body',req.body);


 res.send('erg');
}
exports.reservation =  function(req, res){
 db.connect(function(){console.log('connection base depuis:',scriptName)
    });
 let mydate = db.get_date();
 let dotation = req.params.id;
 db.get().any("select depot, quantite_initiale , quantite_retiree,datedotation, id_produit, comites.libelle as comite_lib,comite, dateretrait, produits.libelle from repartitions join  produits \
 on produit= id_produit  join comites on comite= id_comite  where dotation= $1;",[dotation])
 .then(data =>{
      let strlignes = JSON.stringify(data);
     res.render('une_dotation', { title: 'Dotation'  ,date: mydate, lignes:strlignes   });
  })
 .catch(error => {
        console.log(error);
    });

}
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
  db.get().one("INSERT INTO dotations (depot, produit, datedotation, quantite_initiale, quantite_reservee,origine) VALUES ($1, $2, $3, $4, $5, $6) RETURNING id_dotation",[depot, produit,strdate, dotation, total, 'dotation globale'] )
    .then((data)=> {
      console.log('id', data.id_dotation);
      let dot = data.id_dotation;
      // insert pour chacun des comites
       let tabcomite =[];
       let tabkeys = Object.keys(req.body);
       console.log('er',tabkeys);
       db.get().task(t => {
         for(i=0; i < tabkeys.length;i++){
           if(tabkeys[i][0] != '_') {
             let comite = tabkeys[i];
             let quantite = Number(req.body[tabkeys[i]]);
             tabcomite.push(db.get().none("INSERT INTO repartitions (dotation, depot, produit, datedotation, quantite_initiale, comite, origine)  \
             Values ($1,$2,$3, $4, $5, $6,$7)",[data.id_dotation, depot, produit, strdate, quantite, comite,'reservation globale']  ));
           }
          }
        return t.batch(tabcomite)
      .then(() => {
         res.redirect("/une_dotation/"+ dot);
      })
    })
  })

}
