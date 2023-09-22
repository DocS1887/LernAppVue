<template>
  <div class="row" style="padding-top: 3%">
    <section>
      <div class="col d-flex justify-content-center">
        <RouterLink to="./lesen">
        <div class="card">
            <div class="card-body d-flex flex-column align-items-center">
                <h5 class="card-title">Deutsch</h5>
                <p class="card-text">Ob Buchstaben, Wörter und ganze Texte. Bald kannst du alles lesen :)</p>
            </div>
        </div>
        </RouterLink>
      </div>
    </section>
    <section>
      <div class="col d-flex justify-content-center">
        <RouterLink to="./rechnen">
        <div class="card">
            <div class="card-body d-flex flex-column align-items-center">
                <h5 class="card-title">Mathe</h5>
                <p class="card-text">Plus und Minus sind für dich bald kein Problem mehr!</p>
            </div>
        </div>
        </RouterLink>
      </div>
    </section>
  </div>
</template>

<style scoped>

.card {
    border-radius: 50%;
    width: 22rem;
    text-align: center;
    padding: 2%;
}
a:link {
    text-decoration: none;
}
section {
    padding: 5%;
}


</style>

<script setup>
</script>
