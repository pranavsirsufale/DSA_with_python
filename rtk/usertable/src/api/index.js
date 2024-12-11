import Chance from 'chance'

const chance = Chance()

export const fakeUserData = () => (
     chance.name({ middle : true })
    )