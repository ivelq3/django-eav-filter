<template lang="pug">
div
  b-carousel#carousel(:interval="2000", controls, indicators)
    b-carousel-slide(img-src="https://via.placeholder.com/1400x400")
</template>