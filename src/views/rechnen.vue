
<template>
  <h2>Suche dir eine Übung aus!</h2>
  <div class="row">
    <div class="col">
      <RouterLink to="./zahlenlesen">
      <button type="button" class="btn btn-outline-select">Zahlen lesen</button>
      </RouterLink>
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./plusrechnen">
      <button type="button" class="btn btn-outline-select">Plus rechnen</button>
      </RouterLink>  
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./minusrechnen">
      <button type="button" class="btn btn-outline-select">Minus rechnen</button>
      </RouterLink>  
    </div>
    <div class="col" style="justify-content: center;">
      <RouterLink to="./plusminusrechnen">
      <button type="button" class="btn btn-outline-select">Plus und Minus rechnen</button>
      </RouterLink>  
    </div>
  </div>
</template>
    
    
    
    <style scoped>

    </style>
