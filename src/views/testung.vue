<template>
  <div>
    <p>Startzeit: {{ startTime }}</p>
    <p>Endzeit: {{ endTime }}</p>
    <p>Zeitdifferenz in Minuten: {{ timeDifferenceInMinutes }}</p>
  </div>

 

</template>

<script scoped>
import { parse, differenceInMinutes } from 'date-fns';

export default {
  data() {
    return {
      startTime: '10:00',
      endTime: '14:30',
    };
  },
  computed: {
    timeDifferenceInMinutes() {
      const startDate = parse(this.startTime, 'HH:mm', new Date());
      const endDate = parse(this.endTime, 'HH:mm', new Date());
      return differenceInMinutes(endDate, startDate);
    },
  },
};
</script>

<style >


</style>
