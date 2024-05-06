<template>
    <div class="calendar-order">
      <Calendar v-model="dates" selection-mode="range" :min-date="minDate" :max-date="maxDate" :inline="false" :disabled-dates="unavailableDates" @update:modelValue="emitDates" />
    </div>
</template>
  
<script>
    import axios from 'axios';
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import Calendar from 'primevue/calendar';

    export default {
    methods: {
        emitDates
    },
    components: {
        Calendar
    },
        setup() {
            const router = useRouter();
            const dates = ref(null);
            const unavailableDates = ref([]);

            const minDate = ref(new Date());
            const maxDate = ref(new Date());
            maxDate.value.setFullYear(maxDate.value.getFullYear() + 1);

            const fetchReservedDates = async () => {
            const listingId = router.currentRoute.value.params.id;
            try {
                const response = await axios.get(`/reserved-dates/${listingId}/`);
                console.log("Reserved Dates Response: ", response.data);
                unavailableDates.value = combineDateRanges(response.data); // Process all date ranges
                console.log("Unavailable Dates: ", unavailableDates.value);
            } catch (error) {
                console.error("Error fetching reserved dates:", error);
            }
            };

            onMounted(() => {
            fetchReservedDates();
            });

            return { dates, unavailableDates, minDate, maxDate };
        }
    };
        function expandDateRange(startDate, endDate) {
            const start = new Date(startDate);
            const end = new Date(endDate);
            let dates = [];
            
            for (let dt = new Date(start); dt <= end; dt.setDate(dt.getDate() + 1)) {
                dates.push(new Date(dt)); // Push a copy of dt to avoid mutating the original date
            }

            return dates;
        }

        // Combines multiple date ranges into a single array of disabled dates
        function combineDateRanges(ranges) {
            let allDates = [];
            
            ranges.forEach(range => {
                const dates = expandDateRange(range.start_date, range.end_date);
                allDates = allDates.concat(dates); // Combine dates from each range
            });

            return allDates;
        }

        function emitDates(dates) {
            this.$emit('dates-selected', dates);
        }

</script>
  