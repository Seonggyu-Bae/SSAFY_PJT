<template>
  <div class="popup-dialog" v-if="isOpen">
    <div class="popup-content">
      <h2>추가가 완료되었습니다!</h2>
      <button @click="closePopup">확인</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isOpen: Boolean
  },
  methods: {
    closePopup() {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>
/* 스타일링을 추가할 수 있습니다. */
</style>