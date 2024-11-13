

function Todo() {
  return (
    <div className="container">
        <div className="todo-app">
            <h1>
                <i className="fa-regular fa-pan-to-square"> To do list</i>
            </h1>
            <div className="row">
                <form >
                    <input type="text" id="inputu-box" placeholder="Add a new task" />
                    <button> Add Text</button>
                </form>
            </div>
            <ul id="list-container" ></ul>
        </div>

    </div>
  )
}

export default Todo