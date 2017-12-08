// controleur depots
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db')

function  helper_agrege(produits,depots) {
   let tab_produit = produits;
   let ta_lignes = depots;
   my_hash = {};
   my_hashdep = {}
   for (var i=0; i < tab_produit.length;i++) {
       my_hash[tab_produit[i].id_produit] = tab_produit[i];
   }
   console.log('e',my_hash);

   for (var i=0; i < ta_lignes.length;i++) {
       if (ta_lignes[i].id_depot in my_hashdep) {
                my_hashdep[ta_lignes[i].id_depot].push(ta_lignes[i]);
       }
       else { my_hashdep[ta_lignes[i].id_depot] =[ta_lignes[i]];
       }
   }
   console.log('dep',my_hashdep);
   console.log(Object.keys(my_hashdep))
   return[my_hashdep,my_hash];
};
exports.depot_recap = function(req, res) {
 db.connect(function(){console.log('connection base depuis:',scriptName)
  });
 db.get().task(t => {
    const q3 = t.any("select id_produit, produits.libelle as nom , stock , familles.libelle, couleur from produits inner join familles on famille  = id_famille where stock > 0 order by id_produit;"   ) ;
    const q2 = t.any("select  id_produit,id_depot, SUM(quantite) from mouvement_depot   where  TYPE = 'SORTIE'group by id_depot,id_produit order by id_produit ;");
    return t.batch([q3,q2])
    .then(data => {
               let general = data[0];
               [detail,libel] = helper_agrege(data[0],data[1]);
               res.render('depotrecap', { title: 'Les dépots de laREM94' , general: general,depot: detail, produit: libel});
    })
    })
.catch(error => {
        console.log(error);
    });


}
exports.depot_maj = function(req, res) {
 db.connect(function(){console.log('connection base depuis:',scriptName)
  });
 let myproduit = req.body.produit;
 let quantite  = req.body.quantite;
 let depot     = req.body.depot;
 let madate    = req.body.date;
 db.get().task(t => {
       const q1 = t.none('INSERT INTO mouvement_depot (datemvt,type, quantite, id_produit, id_depot) VALUES($1, $2, $3, $4, $5)', [madate,'SORTIE',quantite,myproduit,depot]);
       const q2 = t.none('UPDATE  produits set stock = stock - $1 where id_produit = $2',[quantite, myproduit]);
      return t.batch([q1,q2])
      .then(() => {
        res.redirect('/');
        // success;
    })
    .catch(error => {
        console.log(error);
    });
    });



}
exports.depot_sortie = function(req, res) {

  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  var hub;
  var madate = new Date();
  var jour=madate.getDate();
  var mois=madate.getMonth()+1;
  var an=madate.getFullYear();
  strdate =an+ '-' + mois + '-' + jour
  db.get().task(t => {
    const q1 = t.any("select id_produit, produits.libelle as nom , stock , familles.libelle, couleur from produits inner join familles on famille  = id_famille where stock > 0;"   ) ;
    const q2 = t.any("SELECT  * from depots where nom  != 'A suivre' order by nom;");
  return t.batch([q1,q2])
  .then(data => {
     console.log("d",data[0])
     res.render('depotsortie', { title: 'Approvisonnement des depots secondaires', produits: data[0],date: strdate, depots: data[1] });
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
exports.depot_entree = function(req, res,next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  var hub;
  var madate = new Date();
  var jour=madate.getDate();
  var mois=madate.getMonth()+1;
  var an=madate.getFullYear();
  strdate =an+ '-' + mois + '-' + jour
  db.get().task(t => {
    const q1 = t.any("select id_produit, produits.libelle as nom , stock , familles.libelle, couleur from produits inner join familles on famille  = id_famille;"   ) ;
  return t.batch([q1])
  .then(data => {
     console.log("d",data[0])
     res.render('depotentree', { title: 'Gestion du dépot départemental', produits: data[0],date: strdate });
  })
  })
  .catch(error => {
        console.log(error);
    });
}


exports.index = function(req, res,next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });
  var hub;
  db.get().task(t => {
    const q1 =   t.one('SELECT  hub from hubs;');
    const q2 = t.one("select count(distinct(id_produit))  from mouvement_depot;");
    const q3 = t.any("select id_produit, produits.libelle as nom , stock , familles.libelle, couleur from produits inner join familles on famille  = id_famille where stock > 0;"   ) ;


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
