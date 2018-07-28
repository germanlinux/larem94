var pgp = require("pg-promise")(/*options*/)
var state = {
  db: null,
};
exports.connect = function(done) {
  if (state.db) return done();
 //     var mybase = process.env.DATABASE_URL +'?ssl=true';
      var mybase = "postgres://postgres:pass@127.0.0.1:5432/larem94"
      state.db =pgp(mybase);
      done()
};
exports.get = function() {
  return state.db;
};
exports.get_date = function(){
var madate = new Date();
  var jour=madate.getDate();
  var mois=madate.getMonth()+1;
  var an=madate.getFullYear();
  strdate =an+ '-' + mois + '-' + jour
  return(strdate);
}
/*
console.log("connection)")
db.one("SELECT  hub from hubs;")
  .then(function(data){
      console.log(data.hub);
  })
  .catch(function(error){
    console.log(error);
  });
*/
