// controleur produits
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db');

// SEPARATEUR

exports.liste= function(req, res) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  db.get().task(t => {
    const q1 =   t.any('select libelle from familles');
    return t.batch([q1])
  .then(data => {
         res.render('familleliste', { title: 'Les familles de produit'  , famille: data[0]  });
    })
    })
  .catch(error => {
        console.log(error);
    });
}
/* gestion d une nouvelle famillet dans le depot */
exports.add = function(req, res) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  let famille = req.body.famille;

  db.get().none("INSERT into familles (libelle,couleur )  values ($1,'panel-lemonchiffon')",[famille])
  .then(() => {
       res.redirect('/famille_list');
  })
  .catch(error => {
        console.log(error);
    });
}
