// controleur depots
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db')
exports.index = function(req, res,next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  var hub;
  db.get().task(t => {
    const q1 =   t.one('SELECT  hub from hubs;');
    const q2 = t.one("select count(distinct(id_produit))  from mouvement_depot;");
    const q3 = t.any("select id_produit, produits.libelle as nom , stock , familles.libelle, couleur from produits inner join familles on famille  = id_famille;"   ) ;


    return t.batch([q1,q2,q3])
    .then(data => {

                    console.log("d", data[0]);
                    console.log("d", data[1].count);
                    console.log("d", data[2]);
                    /*
                    tb =[];
                    for (produit in data[2]) {
                      console.log('produit', produit);
                       cdt = Number(produit)
                       console.log('cdt',cdt)
                      const prdplus  = t.one("select SUM (quantite), id_produit from mouvement_depot where id_produit = $1  and TYPE = 'ENTREE';", [cdt]);
                      const prdmoins = t.one("select SUM (quantite) from mouvement_depot where id_produit = $1  and TYPE = 'SORTIE';", [cdt]);
                      tb.push(prdplus);
                      tb.push(prdmoins);
                    }
                    return(t.batch(tb))
                    */
       let hub  = data.shift().hub;
       let nb = data.shift().count;
       console.log('eg', data.length)
       var eg = data.shift();
      res.render('index', { title: 'Stock laREM94' , manchette: hub , nbproduit: nb, datas: eg});
    })
    })
  .catch(error => {
        console.log(error);
    });


};
//page depot liste des dépots
exports.depot_liste= function(req, res, next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  var hub;
  db.get().task(t => {
    const q1 =   t.any('SELECT  * from depots order by nom;');
    return t.batch([q1])
.then(data => {
     console.log('eg', data);
     let eg = data.shift();
  res.render('depotlist', { title: 'Stock laREM94'  ,  datas: eg});
    })
    })
  .catch(error => {
        console.log(error);
    });
};

// About page route
exports.depot_about= function(req, res) {
  res.render('A propos de l application stocklarem94');
};

