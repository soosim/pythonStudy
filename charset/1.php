<?php
class CircleQueue
{
	const HOST = 'localhost';
	const PORT = '6379';

	public $times;
	public $name;
	public $redis;
	public function __construct($name, $times='3600')
	{
		if (!$name) {
			throw new Exception('Invalid Name');
		}
		$this->name = $name;
		$this->times = $times;
		$this->redis = new Redis();
		$this->_connectRedis();
		$this->createQueue();
	}
}