var pgp = require("pg-promise")(/*options*/)
var state = {
  db: null,
};
exports.connect = function(done) {
  if (state.db) return done();
      state.db =pgp("postgres://larem94:larem94@192.168.99.100:5432/stock94");
      done()
};
exports.get = function() {
  return state.db;
};

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
