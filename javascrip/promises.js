//! promise creation
// const promiseOne = new Promise(function(res,rej){
//     //? Do an async task
//     // DB caslls, caryptography , network

//     setTimeout((function(){
//         console.log('async task is complete')
//         res()
//     }, 1000)
//     )
// })

const lis = ['zero','one','two','three','four','five']




let pointer = 0
const printOneByOne = (lis) => {
    if ( pointer >= lis.length-1 ){
        pointer = 0 
    }
    console.log(lis[pointer])
    pointer++
    return
}

// ! promise creation
const promiseOne = new Promise(function(res,rej){
    setInterval(() => {
        // console.log('async task is completed')
        printOneByOne(lis)
        // res()
        const date = new Date()
        // console.log(`${date.getHours()}: ${date.getMinutes()} :${date.getSeconds().toLocaleString() }` )
        // console.log(date.toLocaleDateString())
        console.log(date.toLocaleTimeString())
    }, 1000);
})


//! promise consumption
promiseOne
.then(function(){
    console.log('Promise is consumed ')
})

// promiseOne
// .then(function(){
//     console.log('promise is constumed')
// })


//! promise consumption




