import type { ToastState } from "../../types/toast"
import styles from './Toast.module.css'
interface ToastProps{
    message : string
    state : ToastState
}

export const Toast = ({message, state}: ToastProps) => {
    return(
        <div className={`${styles.toast} ${styles[state]}`}>
            {message}
        </div>
    )

}