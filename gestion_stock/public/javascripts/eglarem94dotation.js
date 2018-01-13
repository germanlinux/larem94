Vue.component('ligne_emmargement',{
  template: "<tr><td><label>{{ligne.comite_lib}}</label></td><td><input type ='text'  :name='ligne.comite'  v-model='ligne.quantite_initiale' /></td><td><span v-if='ligne._status'>&nbspRETIREE</span><span v-else> &nbsp;<button :id='ligne.comite' @click='clique()'  type='submit' class='btn btn-primary'>RETIRER</button></span></td></tr>",
  props:{
    'ligne' :{type: Object},
    'sendm' :{type: Function}

},
  methods:{
   clique: function(event){
      //alert(this.ligne.comite);
      this.sendm([this.ligne.comite, this.ligne.quantite_initiale, this.ligne.id_repartition]);
     // if (event){
      //
      //   alert(event.target.tagName);

      //}
   }

  }

});
var app= new Vue({
  el: '#app',
  data: {
    lignes:[],
    depot: '',
    libelle: '',
    prd:'',
    param1: '',
    quant1:'',
    id_ligne:'',
  },
  methods: {
     onChildMsg: function(msg) {
        this.param1 = msg[0];
        this.quant1 = msg[1];
        this.id_ligne = msg[2];
        this.$nextTick(function () {
            $("#formulaire").submit();
          });

     }

  }
});
var strcom =document.getElementById('mydata').innerHTML;
strcom = strcom.replace(/&#34;/g,'\"');
strcom = strcom.replace(/&#39;/g,'\'');
strcom=strcom.replace(/null/g, '\"0\"');
//console.log('eric',strcom);
var madate = new Date();
var jour=madate.getDate();
var mois=madate.getMonth()+1;
var an=madate.getFullYear();
var strdate = an+ '-' + mois + '-' + jour
app.lignes = JSON.parse(strcom);
app.depot = app.lignes[0].depot;
app.libelle = app.lignes[0].libelle;
app.prd =app.lignes[0].id_produit
app.lignes.forEach(function( item){
  if (item.dateretrait=="0"){
     // item.dateretrait =strdate;
      item.quantite_retiree= item.quantite_initiale;
      item._status = false;
  }
  else {
      item._status = true;

  }
});
console.log(app.lignes);
