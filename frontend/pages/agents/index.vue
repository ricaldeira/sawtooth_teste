<template>
    <div>
        Agents
    </div>
</template>

<script>
export default {
    layout: "logged",
    middleware: ["auth", "check-auth"]
}
</script>