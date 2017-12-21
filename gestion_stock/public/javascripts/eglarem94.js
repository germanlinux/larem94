Vue.component('comite',{
  template: "<tr><td><label>{{comite.libelle}}</label></td><td><div class='form-group'><input type ='text' v-on:input='updateValue()' :name='comite.id_comite'  v-model='comite.quantite' /></div></td></tr>",
  props:['comite'],
  /*mounted:function(){
    this.formatValues();
  },*/
  methods: {
updateValue: function(){
        console.log("egMAJ");
        this.$emit('input');
     },
formatValues: function(){
     console.log("egpasse");
     this.$refs.quantite.value = Number(this.comite.quantite);
     },
  }
});

var app= new Vue({
  el: '#app',
  data: {
    comites: [],
    somme : 0,
  },

  computed: {
       total: function(){
           return this.comites.reduce(function(sum, comite) {
               //console.log('reduce',sum);
               return sum + comite.quantite;

           },0)

       }
     },
   methods: {
     recalcul: function(){
        this.somme=  this.comites.reduce(function(sum, comite) {
               //console.log('winner',sum);
               return sum + Number(comite.quantite);
           },0)

     }


   }


});
var strcom =document.getElementById('mydata').innerHTML;
strcom = strcom.replace(/&#34;/g,'\"');
strcom=strcom.replace(/null/g, '\"0\"');
//console.log('eric',strcom);
app.comites = JSON.parse(strcom);
app.comites.forEach(function( item){
            item['quantite']  ='';

});
console.log(app.comites);
