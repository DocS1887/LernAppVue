
<template>
  <div class="content">
    <div class="inner-content">
      <h2>Los Ben, lass uns Buchstaben lesen!</h2>
      <div class="row">
        <div class="buchstabenformat">
        <p>{{zufallsbuchstabe}}</p>
      </div>
      </div>
      <div class="row">
        <button type="button" class="btn btn-outline-info" @click="zufallsGenerator">Nächster Buchstabe</button>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      buchstabenArray: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
        "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","ä","Ä","ü","Ü","ö",
        "Ö","ß","au","ei","eu","Eu","Au","Ei","ch","Ch"],
      zufallsbuchstabe: 'Bereit?'
    };
  },
  methods: {
    zufallsGenerator() {
      if(this.buchstabenArray.length > 0) {
        const buchstabenIndex = Math.floor(Math.random() * this.buchstabenArray.length);
        this.zufallsbuchstabe = this.buchstabenArray[buchstabenIndex];
        this.buchstabenArray.splice(buchstabenIndex, 1);
      } else {
        this.zufallsbuchstabe = 'Fertig :)'
      }
    },


  },
}
</script>

<style scoped>
.buchstabenformat{
  font-size: 300px;
  font-weight: 700;
  text-align: center;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.inner-content{
  min-height: 500px;

}

</style>