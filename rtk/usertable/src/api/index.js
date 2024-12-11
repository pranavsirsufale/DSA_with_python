import Chance from 'chance'

const chance = Chance()

export const fakeUserData = () => {
    // retunr 
    console.log(chance.name({ middle : true }))
}

// fakeUserData();