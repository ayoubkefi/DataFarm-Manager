import { BrowserRouter, Route, Routes } from "react-router-dom";
import { OperatorPage } from "./pages/OperatorPage";
import { Sidebar } from "./components/Sidebar/Sidebar";
import styles from './App.module.css'
function App() {
  return (
  <BrowserRouter>
    <div className={styles.layout}>
    <Sidebar />
    <div className={styles.page}>
    <Routes>
      <Route path="/operators" element = {<OperatorPage/>} />
    </Routes>
    </div>
    </div>
  </BrowserRouter>
  )
}

export default App