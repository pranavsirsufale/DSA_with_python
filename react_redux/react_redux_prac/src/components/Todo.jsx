import { useSelector, useDispatch, useStore } from "react-redux";
import { MdDeleteForever } from "react-icons/md";
import { store } from "../store/Store";
import { addTask, delteteTask } from "../store/Store";
import { useState } from "react";

function Todo() {
  const [todo, setTodo] = useState("");
  const tasks = useSelector((state) => state.task);
  const dispatch = useDispatch();
  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(addTask(todo));
    setTodo("");
    return;
  };
  const handleDelete = (index) => {
    dispatch(delteteTask(index));
  };
  return (
    <div className="container">
      <div className="todo-app">
        <h1>
          <i className="fa-regular fa-pan-to-square"> To do list</i>
        </h1>
        <div className="row">
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              id="inputu-box"
              placeholder="Add a new task"
              value={todo}
              onChange={(e) => setTodo(e.target.value)}
            />
            <button> Add Text</button>
          </form>
        </div>
        <div className="todo-container">
          <ul id="list-container">
            {tasks.map((task, index) => (
              <li key={index}>
                <p>
                  {index} {task}
                </p>
                <div>
                  <MdDeleteForever
                    className="icon-style"
                    onClick={() => handleDelete(index)}
                  />
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Todo;
