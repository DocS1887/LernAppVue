<template>
  <h2>Suche dir eine Übung aus!</h2>
  <div class="row">
    <div class="col">
      <RouterLink to="./buchstabenlesen">
      <button type="button" class="btn btn-outline-select">Buchstaben lesen</button>
      </RouterLink>
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./woerterlesen">
      <button type="button" class="btn btn-outline-select">Wörter lesen</button>
      </RouterLink>  
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./leseteppich">
      <button type="button" class="btn btn-outline-select">Leseteppich</button>
      </RouterLink>  
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./geschichtenlesen">
      <button type="button" class="btn btn-outline-select">Geschichten lesen</button>
      </RouterLink>  
    </div>
  </div>
</template>



<style scoped>



</style>
