import { useState } from 'react'
import type { ToastState } from '../types/toast'

export const useToast = () => {
  const [toastState, setToastState] = useState<ToastState | null>(null)
  const [message, setMessage] = useState('')

  const showToast = (msg: string, state: ToastState) => {
    console.log('showToast called with:', msg, state)
    setMessage(msg)
    setToastState(state)
    setTimeout(() => {
      setToastState(null)
    }, 3000)
  }

  return { toastState, message, showToast }
}   