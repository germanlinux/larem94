var express = require('express');
var router = express.Router();
var controller_depots =  require('../controllers/depots.js');
var controller_comites = require('../controllers/comites.js');
var controller_produits = require('../controllers/produits.js');
var controller_familles = require('../controllers/familles.js');


/* GET home page. */

router.get('/', controller_depots.index);
router.get('/index.html',   controller_depots.index);
router.get('/depot_liste',  controller_depots.depot_liste);
router.get('/depot/entree', controller_depots.depot_entree);
router.post('/depot/entree', controller_depots.depot_append);
router.get('/depot/sortie', controller_depots.depot_sortie);
router.post('/depot/sortie', controller_depots.depot_maj);
router.get('/comite_liste', controller_comites.liste);
router.get('/comite/:id', controller_comites.edit);
router.post('/comite/:id', controller_comites.update);
router.get('/depot/recap', controller_depots.depot_recap);
router.get('/produit_list', controller_produits.liste);
router.post('/produit_list', controller_produits.produit_add);

router.get('/famille_list', controller_familles.liste);
router.post('/famille_list', controller_familles.add);

module.exports = router;
