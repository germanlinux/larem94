// controleur produits
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db');

// SEPARATEUR

exports.liste= function(req, res) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  db.get().task(t => {
    const q1 =   t.any('select id_produit, produits.libelle, stock, familles.libelle as famille  from produits inner join familles on famille = id_famille order by stock desc');
    const q2 =   t.any('select id_famille, libelle from familles');
    return t.batch([q1,q2])
  .then(data => {
         res.render('produitliste', { title: 'Les produits'  , produit: data[0], familles:data[1]  });
    })
    })
  .catch(error => {
        console.log(error);
    });
}
exports.depot_append = function(req, res) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
    let myproduit = req.body.produit;
    let quantite  = req.body.quantite;
    let madate    = req.body.date;
    console.log('pass',myproduit);
    if (myproduit)  {
      db.get().task(t => {
       const q1 = t.none('INSERT INTO mouvement_depot (datemvt,type, quantite, id_produit) VALUES($1, $2, $3, $4)', [madate,'ENTREE',quantite,myproduit]);
       const q2 = t.none('UPDATE  produits set stock = stock + $1 where id_produit = $2',[quantite, myproduit]);
      return t.batch([q1,q2])
      .then(() => {
        res.redirect('/');
        // success;
    })
    .catch(error => {
        console.log(error);
    });
    });

    } /* TODO si creation de produit */


}
/* gestion d une entree de produit dans le depot */
exports.produit_add = function(req, res) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  let libelle = req.body.nom;
  let famille = req.body.famille;
  console.log('e', libelle, famille)
  db.get().none('INSERT into produits (libelle,famille, stock )  values ($1,$2, 0)',[libelle, famille])
  .then(() => {
       res.redirect('/produit_list');
  })
  .catch(error => {
        console.log(error);
    });
}
