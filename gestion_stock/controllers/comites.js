// controleur comites
var path = require('path');
var scriptName = path.basename(__filename);
db = require('../db');

exports.liste= function(req, res, next) {
  db.connect(function(){console.log('connection base depuis:',scriptName)
  });

  var hub;
  db.get().task(t => {
    const q1 =   t.any('select libelle,id_depot from comites  order by code_interne,id_depot;');
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
        case 'T13':
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
