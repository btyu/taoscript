idle_threshold=100    # threshold of whether GPU is idle (MB)
busy_sleep=600        # sleep time when GPU is busy (s)


check_gpu_idle () {
  is_idle='true'
  for i in $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)
  do
    if [ "$i" -gt "$idle_threshold" ]
    then
      is_idle='false'
      break
    fi
  done
}


while true
do
  check_gpu_idle
  if [ "$is_idle" = 'true' ]
  then
    echo "Running script..."

    # ===== specify commands here =====
    
    
    # =============

    break
  else
    echo "Since GPU(s) are busy, sleep for a while..."
    sleep $busy_sleep
  fi
done
