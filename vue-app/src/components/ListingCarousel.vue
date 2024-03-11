<template>
    <div>
        <div class="carousel">
        </div>
    </div>
            <div class="carousel-inner">
                <div class="carousel-item">
                    <img src="https://via.placeholder.com/150">
                </div>
                <div class="carousel-item">
                    <img src="https://via.placeholder.com/150">
                </div>
                <div class="carousel-item">
                    <img src="https://via.placeholder.com/150">
                </div>
                <div class="carousel-item">
                    <img src="https://via.placeholder.com/150">
                </div>
    </div>
</template>

<script>
export default {
    name: 'ListingCarousel',
}
</script>

<style scoped>
    .carousel-inner {
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        margin-top: 3%;
        margin-left: 20%;
        margin-right: 20%;
    }
</style>