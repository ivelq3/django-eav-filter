<template>
  <div>
    <b-button v-b-modal.modal-xl variant="primary">xl modal</b-button>

    <b-modal id="modal-xl" size="xl" title="Extra Large Modal"
      >Hello Extra Large Modal!</b-modal
    >
  </div>
</template>

<style scoped>
.modal-dialog {
  max-width: 100%;
  margin: 0;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100vh;
  display: flex;
}
</style>