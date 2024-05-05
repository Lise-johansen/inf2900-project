<template>
    <div class="buttons-container">
        <div class="first-row">
            <Button label="Summer" outlined />
            <Button label="Winter" outlined />
            <Button label="Tools" outlined/>
            <Button label="Electronics" outlined/>
        </div>
        <div class="second-row">
            <Button label="Electronics" outlined/>
            <Button label="Clothing"  outlined/>
            <Button label="Furniture" outlined/>
            <Button label="Sports Equipment" outlined/>
        </div>
    </div>
</template>

<script>
import Button from 'primevue/button';
export default {    
    components: {
        Button
    },
    name: 'FilterButtons',
}
</script>

<style scoped>
    .buttons-container {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        align-content: center;
        justify-content: space-between;
        max-width: 1200px;
        margin: auto auto;
    }
    .p-button {
        margin: 10px;
        transition: outline 200ms ease; 
    }
    .p-button:hover {
        outline: 2px solid var(--primary-color);
    }


</style>