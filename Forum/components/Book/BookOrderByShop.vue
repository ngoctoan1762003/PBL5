<template>
    <div class="py-5">
        <div class="flex bg-[#FFCA42] items-center gap-5 px-5 py-2">
            <div class="w-[20px]">
                <input class="w-[100%] h-[100%]" type="checkbox" @change="handleChange">
            </div>
            <div class="text-[#1B3764] text-[16px] font-semibold">
                {{ shop_name }}
            </div>
            <div>
                >
            </div>
        </div>
        <div class="flex flex-col gap-3">
            <div v-for="book in books" :key="book._id">
                <BookOrderCard :book="book"
                    @checkBoxChecked="addBook"
                    @checkBoxUnchecked="removeBook"
                    @decreaseQuantity="decreaseQuantity"
                    @increaseQuantity="increaseQuantity"
                    @deleteBookFromCart="deleteBookFromCart"
                    @updateQuantity="updateQuantity"
                />
            </div>
        </div>
    </div>
</template>

<script>
import BookOrderCard from '~/components/Book/BookOrderCard.vue'

export default {
    components: {
        BookOrderCard,
    },
    props:{
        books: [],
        shop_name: String,
        shop_id: String,
    },
    methods: {
        handleChange(event) {
            if (event.target.checked) {
                this.add();
            } else {
                this.minus();
            }
        },
        add() {
            this.$emit('addFromShop', this.shop_id);
        },
        minus() {
            this.$emit('removeFromShop', this.shop_id);
        },
        addBook(bookId){
            this.$emit('addBook', bookId, this.shop_id);
        },
        removeBook(bookId){
            this.$emit('removeBook', bookId, this.shop_id);
        },
        increaseQuantity(bookId){
            this.$emit('increaseQuantity', bookId, this.shop_id);
        },
        decreaseQuantity(bookId){
            this.$emit('decreaseQuantity', bookId, this.shop_id);
        },
        deleteBookFromCart(bookId){
            this.$emit('deleteBookFromCart', bookId, this.shop_id);
        },
        updateQuantity(bookId, quantity){
            this.$emit('updateQuantity', bookId, this.shop_id, quantity);
        }
    }
}
</script>
