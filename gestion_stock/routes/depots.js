var express = require('express');
var router = express.Router();
var controller_depots =  require('../controllers/depots.js');
var controller_comites = require('../controllers/comites.js');


/* GET home page. */

router.get('/', controller_depots.index);
router.get('/index.html',   controller_depots.index);
router.get('/depot_liste',  controller_depots.depot_liste);

router.get('/comite_liste', controller_comites.liste);

module.exports = router;
