<template>
    <div class = button-row>
        <button class = "filter-button red" @click="handleButtonClick"></button>
        <button class = "filter-button orange" @click="handleButtonClick"></button>
        <button class = "filter-button orange" @click="handleButtonClick"></button>
        <button class = "filter-button blue" @click="handleButtonClick"></button>
    </div>
</template>

<script>
export default {
    name: 'FilterButtons',
}
</script>

<style scoped>

    .button-row{
        display: flex;
        justify-content: space-evenly;
        margin-top: 3%;
        margin-left: 30%;
        margin-right: 30%;
    }

    .filter-button {
        width: 72px;
        height: 72px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 3px solid black;
        background-image: url('https://via.placeholder.com/72/');
    }

    .filter-button:hover {
        cursor: pointer;
        transform: scale(1.1);
        box-shadow: 0px 0px 5px 2px gray;
        transition: 0.1s;

    }

    .red 
    {
        background-color: #ff5733;
    }

    .orange 
    {
        background-color: #ffa500;

    }

    .blue 
    {
        background-color: #4169e1;

    }


</style>